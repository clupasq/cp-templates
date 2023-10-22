(() => {
    const copyToClipboard = (text) => {
        const dummy = document.createElement("textarea");
        document.body.appendChild(dummy);
        dummy.value = text;
        dummy.select();
        document.execCommand("copy");
        document.body.removeChild(dummy);
    };

    const parseTestBlock = (testBlock) => {
        const test = [null, null];
        for (const c of testBlock.childNodes) {
            if (c.textContent === "Input:") {
                test[0] = c.nextSibling.textContent.trim();
            }
            if (c.textContent === "Output:") {
                test[1] = c.nextSibling.textContent.trim();
            }
        }
        return test;
    };

    const parseTestBlocks = () => {
        const testBlocks = [...document.querySelectorAll("pre")];
        return testBlocks.map(parseTestBlock);
    };

    const getCode = () => {
        let code = "";
        const codeLines = [...document.querySelectorAll(".view-line")];
        for (const l of codeLines) {
            const line = l.textContent.replace(/\s/g, " ");
            code += line + "\n";
        }
        return code
    };

    const getFunctionName = (code) => {
        return code.split("\n")[1].trim().split(/\s/)[1].split("(")[0];
    };

    const code = getCode();
    const fnName = getFunctionName(code);
    const tests = parseTestBlocks();

    let template = "\nfrom typing import List\n";
    template += "try:\n";
    template += "    from icecream import ic\n";
    template += "except ImportError:\n";
    template += "    def ic(*x):\n";
    template += "        return x\n\n";
    template += code;
    template += "    pass\n\nlc_solution = Solution()\n\n";

    for (let i = 0; i < tests.length; i++) {
        const [input, output] = tests[i];
        const test = `def test_example_${i}():\n
    actual = lc_solution.${fnName}(${input})\n
    assert ${output} == actual\n\n`;
        template += test
    }
    copyToClipboard(template);
})()
