(() => {
    const copyToClipboard = (text) => {
        const dummy = document.createElement("textarea");
        document.body.appendChild(dummy);
        dummy.value = text;
        dummy.select();
        document.execCommand("copy");
        document.body.removeChild(dummy);
    };

    const getTests = () => {
        const strongs = [...document.querySelectorAll("strong")];
        const inputLabels = strongs.filter(s => s.textContent === "Input:");
        return inputLabels.map(l => {
            let input = "";
            let crtEl = l.nextSibling;
            while (crtEl.textContent !== "Output:") {
                input += crtEl.textContent;
                crtEl = crtEl.nextSibling;
            }
            const output = crtEl.nextSibling;
            return [
                input.trim(),
                output.textContent.trim()
            ]
        });
    };

    const getCode = (lang="python3") => {
        const def = pageData.codeDefinition.find(r => r.value === lang);
        return def.defaultCode;
    };

    const getFunctionName = (code) => {
        return code.split("\n")[1].trim().split(" ")[1].split("(")[0];
    };

    const code = getCode();
    const fnName = getFunctionName(code);
    const tests = getTests();

    let template = "from typing import List\n";
    template += "try:\n";
    template += "    from icecream import ic\n";
    template += "except ImportError:\n";
    template += "    def ic(x=None):\n";
    template += "        return x\n\n";
    template += code;
    template += "pass\n\nlc_solution = Solution()\n\n";

    for (let i = 0; i < tests.length; i++) {
        const [input, output] = tests[i];
        const test = `def test_example_${i}():\n    actual = lc_solution.${fnName}(${input})\n    assert ${output} == actual\n\n`;
        template += test
    }

    copyToClipboard(template);
})()
