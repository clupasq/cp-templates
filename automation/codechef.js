(((d) => {
    const copyToClipboard = (text) => {
        const dummy = d.createElement("textarea");
        d.body.appendChild(dummy);
        dummy.value = text;
        dummy.select();
        d.execCommand("copy");
        d.body.removeChild(dummy);
    };
    const formatIoSample = (s) => {
        const lines = s.split("\n");
        /* Erase last two lines, if empty.*/
        if (!lines[lines.length - 1].match(/\S/)) {
            lines.pop();
        }        if (!lines[lines.length - 1].match(/\S/)) {
            lines.pop();
        }        return lines.join("\n");
    };
    const sampleInput = document.querySelector('#sampleinput + pre>code');
    const sampleOutput = document.querySelector('#sampleoutput + pre>code');
    const input = formatIoSample(sampleInput.textContent);
    const output = formatIoSample(sampleOutput.textContent);
    const commands = `echo '${input}' > input.txt\n        echo '${output}' > output.txt\n`;
    copyToClipboard(commands);
})(document));

