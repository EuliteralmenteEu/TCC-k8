document.getElementById('form-cadastro').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;
    const alertBox = document.getElementById('alert-box');
    const successBox = document.getElementById('success-box');
    alertBox.classList.add('d-none');
    successBox.classList.add('d-none');
    
    if (password !== confirmPassword) {
        alertBox.textContent = 'As senhas não coincidem.';
        alertBox.classList.remove('d-none');
        return;
    }
    
    try {
        const response = await fetch('/api/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nome, email, password })
        });
        
        const data = await response.json();
        
        if (response.ok && data.success) {
            successBox.textContent = 'Conta criada com sucesso! Redirecionando...';
            successBox.classList.remove('d-none');
            document.getElementById('form-cadastro').reset();
            setTimeout(() => {
                window.location.href = '/';
            }, 2000);
        } else {
            alertBox.textContent = data.error || 'Erro ao criar conta.';
            alertBox.classList.remove('d-none');
        }
    } catch (error) {
        console.error('Erro:', error);
        alertBox.textContent = 'Erro ao conectar ao servidor.';
        alertBox.classList.remove('d-none');
    }
});
