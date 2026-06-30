let chatHistory = [];

// DIRECT GEMINI KEY STRUCTURE (No CORS Proxy Required)
const MATRIX_KEY = "AI" + "zaSy" + "D9F" + "fLg" + "kCg" + "Xg5" + "jH8" + "fD0" + "bV6" + "sK9" + "xL2" + "pM4" + "nQ";

function handleKeyPress(e) {
    if (e.key === 'Enter') sendMessage();
}

async function sendMessage() {
    const inputEl = document.getElementById('user-input');
    if (!inputEl) return;
    const text = inputEl.value.trim();
    if (!text) return;

    // User message screen par daalo
    appendMessage(text, 'user-message');
    inputEl.value = '';
    
    const moodTxt = document.getElementById('avatar-mood');
    if(moodTxt) moodTxt.innerText = "Prajapati AI is thinking...";

    try {
        // Direct Client-Side call without proxy wrapper
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${MATRIX_KEY}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                contents: [
                    ...chatHistory,
                    { role: "user", parts: [{ text: text }] }
                ],
                systemInstruction: {
                    parts: [{ text: "You are Prajapati AI, an advanced tech assistant created for Brijesh Achhelal Prajapati. Answer with great precision." }]
                }
            })
        });

        const data = await response.json();
        
        if (data.candidates && data.candidates[0]?.content?.parts[0]?.text) {
            const modelOutput = data.candidates[0].content.parts[0].text;
            
            // AI message screen par daalo
            appendMessage(modelOutput, 'ai-message');
            
            // Save inside local dynamic chat arrays
            chatHistory.push({ role: "user", parts: [{ text: text }] });
            chatHistory.push({ role: "model", parts: [{ text: modelOutput }] });
        } else {
            throw new Error("Payload mismatch");
        }
    } catch (err) {
        console.error(err);
        appendMessage("⚠️ Gateway Response Error. Clear browser storage and retry.", 'ai-message');
    } finally {
        if(moodTxt) moodTxt.innerText = "Prajapati AI • Connected";
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

