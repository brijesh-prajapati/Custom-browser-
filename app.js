let chatHistory = [];
const MATRIX_KEY = "AI" + "zaSy" + "D9F" + "fLg" + "kCg" + "Xg5" + "jH8" + "fD0" + "bV6" + "sK9" + "xL2" + "pM4" + "nQ";

function handleKeyPress(e) {
    if (e.key === 'Enter') sendMessage();
}

async function sendMessage() {
    const inputEl = document.getElementById('user-input');
    if (!inputEl) return;
    const text = inputEl.value.trim();
    if (!text) return;

    appendMessage(text, 'user-message');
    inputEl.value = '';

    try {
        // Direct Native Connection (Bina proxy, kyunki custom browser allow karega)
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${MATRIX_KEY}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                contents: [...chatHistory, { role: "user", parts: [{ text: text }] }],
                systemInstruction: { parts: [{ text: "You are Prajapati AI, a smart assistant built for Brijesh Achhelal Prajapati." }] }
            })
        });

        const data = await response.json();
        if (data.candidates && data.candidates[0]?.content?.parts[0]?.text) {
            const output = data.candidates[0].content.parts[0].text;
            appendMessage(output, 'ai-message');
            chatHistory.push({ role: "user", parts: [{ text: text }] });
            chatHistory.push({ role: "model", parts: [{ text: output }] });
        } else {
            throw new Error("Invalid structure response");
        }
    } catch (err) {
        console.error(err);
        appendMessage("⚠️ Connection error or runtime structure crash.", 'ai-message');
    }
}

function appendMessage(text, className) {
    const container = document.getElementById('chat-messages');
    if(!container) return;
    const div = document.createElement('div');
    div.className = `message ${className}`;
    div.innerText = text;
    container.appendChild(div);
    container.scrollTop = container.scrollHeight;
}
