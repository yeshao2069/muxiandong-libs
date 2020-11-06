'use strict';

const iconv = require('iconv-lite'); 

exports.style = `
section { padding: 0 4px; font-size: 10px; }
.profit { color: var(--color-danger-fill); }
.loss { color: var(--color-success-border); }
`;

exports.template = `
<section>-</section>
`;

exports.$ = {
    section: 'section',
};

const config = {
    current: '',
    interval: 20,
    numerical: true,
    amplitude: false,
};

exports.methods = {
    /**
     * 从编辑器配置系统读取配置，缓存到变量里
     */
    async updateConfig() {
        config.current = await Editor.Profile.getConfig('stock', 'current');
        config.interval = await Editor.Profile.getConfig('stock', 'interval');
        config.numerical = await Editor.Profile.getConfig('stock', 'numerical');
        config.amplitude = await Editor.Profile.getConfig('stock', 'amplitude');
        this.update(true);
    },

    /**
     * 更新股票数据
     * @param {boolean} force 是否强制刷新
     */
    async update(force = false) {
        clearTimeout(this.timer);

        if (!config.current) {
            this.$.section.innerHTML = '-';
            this.$.section.classList.remove('loss');
            this.$.section.classList.remove('profit');
            return;
        }

        const date = new Date();
        const hour = date.getHours();
        const minute = date.getMinutes();

        // 9 点 15 前不需要循环请求数据
        // 15 点之后不需要循环请求
        // 前后各给 1 分钟缓冲
        const allow = (hour > 9 || hour === 9 && minute > 14) && (hour < 15 || hour === 15 && minute < 1);

        if (force || allow) {
            try {
                const buffer = await Editor.Network.get(`http://hq.sinajs.cn/list=${config.current}`);
                const text = iconv.decode(buffer, 'gbk');
                const results = text.replace(/^[^\"]+"/, '').replace(/\"\;$/, '').split(',');
    
                // 生成显示内容
                let string = '';
                if (config.numerical) {
                    const numerical = parseFloat(results[3]).toFixed(2);
                    string += string ? ` ${numerical}` : numerical;
                }
                if (config.amplitude) {
                    const amplitude = ((parseFloat(results[3]) / parseFloat(results[2]) - 1) * 100).toFixed(2) + '%'
                    string += string ? ` ${amplitude}` : amplitude;
                }
                this.$.section.innerHTML = string;
    
                if (parseFloat(results[3]) > parseFloat(results[2])) {
                    this.$.section.classList.remove('loss');
                    this.$.section.classList.add('profit');
                } else {
                    this.$.section.classList.add('loss');
                    this.$.section.classList.remove('profit');
                }
    
            } catch (error) {
                console.warn(error);
                this.$.section.innerHTML = '-';
                this.$.section.classList.remove('loss');
                this.$.section.classList.remove('profit');
            }
        }

        this.timer = setTimeout(() => {
            this.update();
        }, config.interval * 1000);
    }
};

exports.ready = async function() {
    this.updateConfig();
    // 生成一个临时函数，因为 close 的时候需要解绑事件
    // 如果直接绑定 this.update 的话，this 指向不对
    this._update = () => {
        this.updateConfig()
    };
    Editor.Message.addBroadcastListener('stock:update', this._update);
};

exports.close = function() {
    clearTimeout(this.timer);
    Editor.Message.removeBroadcastListener('stock:update', this._update);
};