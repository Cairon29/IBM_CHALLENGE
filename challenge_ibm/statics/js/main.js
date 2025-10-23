console.log('testing testing');


async function sendMessage() {
    const input = document.getElementById('fileInput');
    const textArea = document.getElementById('textAreaInput');
    const file = input.files[0];
    const responseDiv = document.getElementById('summary_result');
    const message = textArea.value;

    if (!message && !file) {
        alert('Please provide text or select a file!');
        return;
    }

    const formData = new FormData();
    formData.append('message', message)
    
    if (file) {
        formData.append('file', file);
    }

    try {
        console.log('Sending request to /analyze/ endpoint');
        console.log('FormData contents:');
        for (let pair of formData.entries()) {
            console.log(`${pair[0]}: ${pair[1]}`);
        }
        const response = await fetch('/analyze/', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        console.log(data);

        if (data.summary_result) {
            const summary = data.summary_result
            console.log(summary);
            responseDiv.innerHTML = `<strong>Summary:</strong> ${summary}`;
            responseDiv.style.backgroundColor = '#d4edda';
        } else {
            responseDiv.innerHTML = `<strong>Error:</strong> ${data.error}`;
            responseDiv.style.backgroundColor = '#f8d7da';
        }

        input.value = '';
        textArea.value = '';
    } catch (error) {
        responseDiv.innerHTML = `<strong>Network Error:</strong> ${error.message}`;
        responseDiv.style.backgroundColor = '#f8d7da';
    }
}

document.getElementById('textAreaInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});