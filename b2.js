document.getElementById('calculator-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const a = parseFloat(document.getElementById('a').value);
    const b = parseFloat(document.getElementById('b').value);

    const fetchData = async (url, data) => {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        return response.json();
    };

    const urls = {
        add: 'http://127.0.0.1:8000/add',
        subtract: 'http://127.0.0.1:8000/subtract',
        multiply: 'http://127.0.0.1:8000/multiply',
        divide: 'http://127.0.0.1:8000/divide'
    };

    const data = { a, b };

    const addResult = await fetchData(urls.add, data);
    const subtractResult = await fetchData(urls.subtract, data);
    const multiplyResult = await fetchData(urls.multiply, data);
    const divideResult = await fetchData(urls.divide, data);

    document.getElementById('add-result').textContent = addResult.result || addResult.error;
    document.getElementById('subtract-result').textContent = subtractResult.result || subtractResult.error;
    document.getElementById('multiply-result').textContent = multiplyResult.result || multiplyResult.error;
    document.getElementById('divide-result').textContent = divideResult.result || divideResult.error;
});