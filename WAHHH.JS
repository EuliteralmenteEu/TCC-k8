document.getElementById('loginForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const emailValue = emailInput.value.trim();
    const passwordValue = passwordInput.value;

    const emailError = document.getElementById('emailError');
    const passwordError = document.getElementById('passwordError');

    if (!validateForm(emailValue, passwordValue, emailError, passwordError)) {
        return;
    }

    await submitLogin(emailValue, passwordValue, emailInput, passwordInput, emailError, passwordError);
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
    }

    return isValid;
}


async function submitLogin(email, password, emailInput, passwordInput, emailError, passwordError) {
    const submitBtn = document.querySelector('button[type="submit"]');
    submitBtn.disabled = true;
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Conectando...';

    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include',
            body: JSON.stringify({ email, password })
        });

        if (response.ok) {
            window.location.href = '/dashboard';
        } else {
            emailError.textContent = 'Email ou senha inválidos.';
            document.getElementById('email').classList.add('invalid');
        }
    } catch (error) {
        emailError.textContent = 'Erro ao conectar. Tente novamente.';
        document.getElementById('email').classList.add('invalid');
        console.error('Login error:', error);
    } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
    }
}
