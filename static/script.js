console.log("script.js loaded");

document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("chat-form");
    const input = document.getElementById("question");
    const chatBox = document.getElementById("chat-box");

    console.log("Form:", form);

    form.addEventListener("submit", async function(e){

        console.log("Submit intercepted");

        e.preventDefault();

        const question = input.value.trim();

        if(question === "") return;

        chatBox.innerHTML += `
        <div class="response user">
            <strong>You:</strong><br>
            ${question}
        </div><br>
        `;

        input.value = "";

        chatBox.innerHTML += `
        <div class="response" id="loading">
            <strong>Fermah AI:</strong><br>
            Thinking...
        </div><br>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

        try{

            const response = await fetch("/chat",{

                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify({
                    question:question
                })

            });

            const data = await response.json();

            document.getElementById("loading").remove();

            chatBox.innerHTML += `
            <div class="response ai">
                <strong>Fermah AI:</strong><br>
                ${data.reply}
            </div><br>
            `;

            chatBox.scrollTop = chatBox.scrollHeight;

        }
        catch(error){

            console.error(error);

        }

    });

});