// ========== 视觉小说引擎 ==========
const AFFINITY_NAMES = { yn: '八奈见', sy: '烧盐', xj: '小鞠', by: '白玉', max: '天爱星', zmx: '志喜屋', js: '佳树' };
const CHAR_COLORS = {
  WZ:'#7ec8e3', YN:'#ffa07a', SY:'#ffd700', XJ:'#dda0dd', BY:'#ffb6c1', MAX:'#ff6347',
  JS:'#98fb98', ZMX:'#c0c0c0', FYH:'#b8860b', YJ:'#87ceeb', YZM:'#ee82ee', YM:'#9370db',
  GX:'#f0e68c', XB:'#ff69b4'
};
const CHAR_NAMES = {
  WZ:'温水和彦', YN:'八奈见杏菜', SY:'烧盐柠檬', XJ:'小鞠知花', BY:'白玉璃子', MAX:'马剃天爱星',
  JS:'温水佳树', ZMX:'志喜屋梦子', FYH:'放虎原云雀', YJ:'樱井弘人', YZM:'月之木古都', YM:'玉木慎太郎',
  GX:'甘夏古奈美', XB:'小拔小夜'
};
const BG_COLORS = {
  black:'#000', restaurant:'#2d1f1a', classroom:'#3a3a4a', hallway:'#4a4a3a',
  clubroom:'#3a2f1a', rooftop:'#1a2f3f', track:'#2f3a1a', infirmary:'#4a5a5a',
  shrine:'#1a1a3f', station:'#3f3a2a', gym:'#4a4a2f', printroom:'#3a3a3f',
  bridge:'#2a3f4f', cafe:'#3a2f2f', beach:'#1a3f5f', wedding:'#5a4a5a'
};

class VisualNovel {
  constructor() {
    this.affinity = { yn:0, sy:0, xj:0, by:0, max:0, zmx:0, js:0 };
    this.scriptIdx = 0;
    this.script = [];
    this.labelMap = {};
    this.running = false;
    this.typing = false;
    this.typingTimer = null;
    this.typingIdx = 0;
    this.typingText = '';
    this.choiceMode = false;
    this.currentRoute = '';
    this.currentBg = 'black';
    this._bindEvents();
    this.el = {
      bg: document.getElementById('bg-layer'),
      char: document.getElementById('char-layer'),
      name: document.getElementById('name-tag'),
      text: document.getElementById('dialogue-text'),
      choices: document.getElementById('choices'),
      overlay: document.getElementById('overlay'),
      indicator: document.getElementById('indicator'),
      dbox: document.getElementById('dialogue-box'),
      menu: document.getElementById('save-menu'),
      menuBtn: document.getElementById('menu-btn')
    };
    this._showTitle();
  }

  loadScript(data) {
    this.script = data;
    this._buildLabelMap();
  }

  _buildLabelMap() {
    this.labelMap = {};
    for (let i = 0; i < this.script.length; i++) {
      if (this.script[i].label) this.labelMap[this.script[i].label] = i;
    }
  }

  _bindEvents() {
    this.el.dbox.addEventListener('click', () => { if (!this.choiceMode) this.advance(); });
    document.addEventListener('keydown', e => {
      if (e.code === 'Space' || e.code === 'Enter') { e.preventDefault(); if (!this.choiceMode) this.advance(); }
      if (e.code === 'Escape') { e.preventDefault(); this.toggleMenu(); }
    });
    window.addEventListener('beforeunload', () => this._autoSave());
  }

  _showTitle() {
    this._setBg('black');
    this.el.name.textContent = '';
    this.el.text.textContent = '';
    this.el.choices.innerHTML = '';
    this.el.overlay.innerHTML = '<h1>败北女角太多了！</h1><p>～青春挽回作战～</p><p style="font-size:16px;color:#888">石蕗高中文艺社，一群在恋爱中败下阵来的女孩<br>她们的逞强、成长，以及新的开始</p><button class="btn" onclick="VN.startGame()">开始游戏</button><button class="btn" onclick="VN.loadGame()" style="margin-top:8px">继续游戏</button><p style="font-size:13px;color:#666;margin-top:12px">空格/回车推进对话 · 点击选项选择 · Esc 菜单</p>';
    this.el.overlay.style.display = 'flex';
    this.el.indicator.style.display = 'none';
    this.el.menuBtn.style.display = 'none';
    this.running = false;
  }

  startGame() {
    this.affinity = { yn:0, sy:0, xj:0, by:0, max:0, zmx:0, js:0 };
    this.scriptIdx = 0;
    this.running = true;
    this.el.overlay.style.display = 'none';
    this.el.indicator.style.display = 'block';
    this.el.menuBtn.style.display = 'block';
    this._execNext();
  }

  restart() { this.toggleMenu(); this.startGame(); }

  advance() {
    if (!this.running) return;
    if (this.typing) { this._finishTyping(); return; }
    this._execNext();
  }

  _execNext() {
    if (this.scriptIdx >= this.script.length) { this._showEnd(); return; }
    const cmd = this.script[this.scriptIdx];
    this.scriptIdx++;
    switch (cmd.type) {
      case 'bg': this._setBg(cmd.id); this._execNext(); break;
      case 'narrate': this._showNarration(cmd.text); break;
      case 'dialogue': this._showDialogue(cmd.char, cmd.text); break;
      case 'choice': this._showChoice(cmd); break;
      case 'affinity': this.affinity[cmd.char] = (this.affinity[cmd.char]||0) + cmd.val; this._execNext(); break;
      case 'jump': this.scriptIdx = this.labelMap[cmd.target]; this._execNext(); break;
      case 'route': this._routeSelect(); break;
      case 'end': this._showEnding(cmd); break;
      default: this._execNext();
    }
  }

  _setBg(id) {
    const c = BG_COLORS[id] || '#222';
    this.el.bg.style.background = c;
    this.currentBg = id;
  }

  _showNarration(text) {
    this.choiceMode = false;
    this.el.choices.innerHTML = '';
    this.el.name.textContent = '';
    this._typeText(text);
  }

  _showDialogue(char, text) {
    this.choiceMode = false;
    this.el.choices.innerHTML = '';
    this.el.name.textContent = CHAR_NAMES[char] || char;
    this.el.name.style.color = CHAR_COLORS[char] || '#fff';
    this._typeText(text);
  }

  _typeText(text) {
    this.typing = true;
    this.typingText = text;
    this.typingIdx = 0;
    this.el.text.textContent = '';
    this.el.indicator.style.display = 'none';
    clearInterval(this.typingTimer);
    this.typingTimer = setInterval(() => {
      if (this.typingIdx < this.typingText.length) {
        this.el.text.textContent += this.typingText[this.typingIdx];
        this.typingIdx++;
      } else {
        clearInterval(this.typingTimer);
        this.typing = false;
        this.el.indicator.style.display = 'block';
      }
    }, 35);
  }

  _finishTyping() {
    clearInterval(this.typingTimer);
    this.el.text.textContent = this.typingText;
    this.typing = false;
    this.el.indicator.style.display = 'block';
  }

  _showChoice(cmd) {
    this.choiceMode = true;
    this.typing = false;
    clearInterval(this.typingTimer);
    this.el.indicator.style.display = 'none';
    this.el.choices.innerHTML = cmd.options.map((opt, i) =>
      '<button class="choice-btn" onclick="VN._pickChoice(' + i + ')">' + opt.text + '</button>'
    ).join('');
  }

  _pickChoice(i) {
    const cmd = this.script[this.scriptIdx - 1];
    const opt = cmd.options[i];
    if (opt.affinity) this.affinity[opt.affinity.char] = (this.affinity[opt.affinity.char]||0) + opt.affinity.val;
    this.choiceMode = false;
    this.el.choices.innerHTML = '';
    this.scriptIdx = this.labelMap[opt.next];
    this._execNext();
  }

  _routeSelect() {
    const aff = this.affinity;
    const routes = [
      { key:'yn', name:'route_yanaami', val:aff.yn||0 },
      { key:'sy', name:'route_yakishio', val:aff.sy||0 },
      { key:'xj', name:'route_komari', val:aff.xj||0 },
      { key:'by', name:'route_shiratama', val:aff.by||0 },
      { key:'max', name:'route_tengoku', val:aff.max||0 }
    ];
    routes.sort((a,b) => b.val - a.val);
    let route = routes[0].name;
    if ((aff.zmx||0) >= 5) route = 'route_shikishi';
    else if ((aff.js||0) >= 6) route = 'route_kaju';
    else {
      const vals = routes.map(r => r.val);
      if (Math.max(...vals) - Math.min(...vals) <= 1) route = 'route_harem';
    }
    this.currentRoute = route;
    if (this.labelMap[route] !== undefined) {
      this.scriptIdx = this.labelMap[route];
    }
    this._execNext();
  }

  _showEnding(cmd) {
    this.running = false;
    this.el.choices.innerHTML = '';
    this.el.indicator.style.display = 'none';
    this._setBg('black');
    this.el.name.textContent = '';
    this.el.text.textContent = '';
    const score = (this.affinity.yn||0)+(this.affinity.sy||0)+(this.affinity.xj||0)+(this.affinity.by||0)+(this.affinity.max||0)+(this.affinity.zmx||0)+(this.affinity.js||0);
    this.el.overlay.innerHTML = '<h1>' + (cmd.title || 'END') + '</h1><p>' + (cmd.subtitle || '') + '</p><p style="font-size:16px;color:#888">好感度总分: ' + score + '</p><button class="btn" onclick="VN.startGame()">重新开始</button><button class="btn" onclick="VN._showTitle()" style="margin-top:8px">返回标题</button>';
    this.el.overlay.style.display = 'flex';
    this.el.menuBtn.style.display = 'none';
  }

  _showEnd() {
    this.running = false;
    this.el.choices.innerHTML = '';
    this.el.indicator.style.display = 'none';
    this._setBg('black');
    this.el.name.textContent = '';
    this.el.text.textContent = '';
    this.el.overlay.innerHTML = '<h1>STAFF</h1><p>原作：雨森たきび《败北女角太多了！》</p><p>改编：dacmh</p><p>「我们败北女角，永不认输。」——文艺社全员</p><button class="btn" onclick="VN.startGame()">重新开始</button><button class="btn" onclick="VN._showTitle()" style="margin-top:8px">返回标题</button>';
    this.el.overlay.style.display = 'flex';
  }

  saveGame() {
    this.toggleMenu();
    const data = { idx: this.scriptIdx, aff: this.affinity, route: this.currentRoute, bg: this.currentBg };
    localStorage.setItem('makeine_vn_save', JSON.stringify(data));
    this._flashMsg('已保存');
  }

  loadGame() {
    this.toggleMenu();
    const raw = localStorage.getItem('makeine_vn_save');
    if (!raw) { this._flashMsg('没有存档'); return; }
    const data = JSON.parse(raw);
    this.scriptIdx = data.idx;
    this.affinity = data.aff;
    this.currentRoute = data.route;
    if (data.bg) this._setBg(data.bg);
    this.running = true;
    this.el.overlay.style.display = 'none';
    this.el.indicator.style.display = 'block';
    this.el.menuBtn.style.display = 'block';
    this._execNext();
  }

  _autoSave() {
    const data = { idx: this.scriptIdx, aff: this.affinity, route: this.currentRoute, bg: this.currentBg };
    localStorage.setItem('makeine_vn_auto', JSON.stringify(data));
  }

  toggleMenu() {
    const m = this.el.menu;
    m.style.display = m.style.display === 'flex' ? 'none' : 'flex';
  }

  _flashMsg(msg) {
    const d = document.createElement('div');
    d.textContent = msg;
    d.style.cssText = 'position:fixed;top:20px;left:50%;transform:translateX(-50%);background:rgba(0,0,0,.8);color:#fff;padding:10px 24px;border-radius:6px;z-index:99;font-size:18px';
    document.body.appendChild(d);
    setTimeout(() => d.remove(), 1500);
  }
}

const VN = new VisualNovel();
