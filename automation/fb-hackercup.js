((() => {
    const elements = [...document.querySelectorAll('span[role=heading]+span[value]')];
    const copyToClipboard = (text) => {        const dummy = document.createElement("textarea");
        document.body.appendChild(dummy);
        dummy.value = text;
        dummy.select();
        document.execCommand("copy");
        document.body.removeChild(dummy);
    };
    copyToClipboard(`echo '${elements[0].getAttribute('value').slice(0, -1)}' > input.txt\necho '${elements[1].getAttribute('value').slice(0, -1)}' > output.txt\n`);
})());

