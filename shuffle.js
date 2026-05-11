function shuffle() {
    const container = document.getElementById("rl");
    const children = Array.from(container.childNodes);
    for (s of children) {
        s.remove();
    }
    for (let i = children.length - 1; i >= 1; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [children[i], children[j]] = [children[j], children[i]];
    }
    for (s of children) {
        container.append(s);
    }
}
new Promise(resolve => {
    if (document.readyState == "loading") {
        document.addEventListener("DOMContentLoaded", resolve);
    } else {
        resolve();
    }
}).then(shuffle);
