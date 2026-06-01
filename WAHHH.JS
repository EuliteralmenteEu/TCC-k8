
document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const emailValue = emailInput.value.trim();
    const passwordValue = passwordInput.value.trim();

    const emailError = document.getElementById('emailError');
    const passwordError = document.getElementById('passwordError');

    
    if (!validateForm(emailValue, passwordValue, emailError, passwordError)) {
        return;
    }

    
    submitLogin(emailValue, passwordValue);
});


function validateForm(email, password, emailError, passwordError) {
    let isValid = true;

    
    emailError.textContent = '';
    passwordError.textContent = '';
    document.getElementById('email').classList.remove('invalid');
    document.getElementById('password').classList.remove('invalid');

    
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email) {
        emailError.textContent = 'Email é necessário.';
        document.getElementById('email').classList.add('invalid');
        isValid = false;
    } else if (!emailRegex.test(email)) {
        emailError.textContent = 'Digite um e-mail válido.';
        document.getElementById('email').classList.add('invalid');
        isValid = false;
    }

    
    if (!password) {
        passwordError.textContent = 'Senha é necessária.';
        document.getElementById('password').classList.add('invalid');
        isValid = false;
    } else if (password.length < 6) {
        passwordError.textContent = 'A senha deve ter pelo menos 6 caracteres.';
        document.getElementById('password').classList.add('invalid');
        isValid = false;
    }

    return isValid;
}


async function submitLogin(email, password) {
    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        if (response.ok) {
            
            window.location.href = '/dashboard';
        } else {
            alert('Email ou senha inválidos.');
        }
    } catch (error) {
        alert('Erro ao conectar. Tente novamente.');
        console.error('Login error:', error);
    }
}
