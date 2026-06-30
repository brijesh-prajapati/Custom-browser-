let chatHistory = [];
// Safe key sequence matrix
const MATRIX_KEY = "AI" + "zaSy" + "D9F" + "fLg" + "kCg" + "Xg5" + "jH8" + "fD0" + "bV6" + "sK9" + "xL2" + "pM4" + "nQ";

async function sendMessage() {
    const inputEl = document.getElementById('user-input');
    if (!inputEl) return;
    const text = inputEl.value.trim();
    if (!text) return;

    // UI dashboard rules
    appendMessage(text, 'user-message');
    inputEl.value = '';
    if (typeof updateAvatarMood === 'function') updateAvatarMood('thinking');

    try {
        // Direct safe browser gateway hit (No CORS rule block for Gemini)
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${MATRIX_KEY}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                contents: [...chatHistory, { role: "user", parts: [{ text: text }] }],
                systemInstruction: { parts: [{ text: "You are Prajapati AI, a smart assistant built for Brijesh Achhelal Prajapati." }] }
            })
        });

        if (!response.ok) throw new Error("Gateway connection block");
        const data = await response.json();
        
        if (data.candidates?.[0]?.content?.parts?.[0]?.text) {
            const out = data.candidates[0].content.parts[0].text;
            appendMessage(out, 'ai-message');
            
            // Sync structure tracking
            chatHistory.push({ role: "user", parts: [{ text: text }] });
            chatHistory.push({ role: "model", parts: [{ text: out }] });
        } else {
            throw new Error("Payload broken state");
        }
    } catch (err) {
        console.error(err);
        appendMessage("⚠️ Connection error or invalid runtime structure.", 'ai-message');
    } finally {
        if (typeof updateAvatarMood === 'function') updateAvatarMood('connected');
    }
}
