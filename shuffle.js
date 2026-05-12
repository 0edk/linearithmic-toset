function shuffle() {
    const container = document.getElementById("rl");
    const children = Array.from(container.childNodes);
    for (s of children) {
        s.remove();
    }
    // https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#JavaScript_implementation
    for (let i = children.length - 1; i >= 1; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [children[i], children[j]] = [children[j], children[i]];
    }
    for (s of children) {
        container.append(s);
    }
}
// https://old.reddit.com/r/Anki/comments/103b97l/help_javascript_template_code_only_works_on_first/j2zsp36/
new Promise(resolve => {
    if (document.readyState == "loading") {
        document.addEventListener("DOMContentLoaded", resolve);
    } else {
        resolve();
    }
}).then(shuffle);
