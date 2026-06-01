// script.js
document.getElementById('INDEX.html').addEventListener('submit', function(e) {
    e.preventDefault();

    
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const emailValue = emailInput.value.trim();
    const passwordValue = passwordInput.value.trim();

    
    const emailError = document.getElementById('emailError');
    const passwordError = document.getElementById('passwordError');

    
    let isValid = true;

    
    emailError.textContent = '';
    passwordError.textContent = '';
    emailInput.classList.remove('invalid');
    passwordInput.classList.remove('invalid');

    
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (emailValue === '') {
        emailError.textContent = 'Email é necessario bobão.';
        emailInput.classList.add('invalid');
        isValid = false;
    } else if (!emailRegex.test(emailValue)) {
        emailError.textContent = 'entre um E-mail valido.';
        emailInput.classList.add('invalid');
        isValid = false;
    }

    
    if (passwordValue === '') {
        passwordError.textContent = 'SENHA é necessaria .';
        passwordInput.classList.add('invalid');
        isValid = false;
    } else if (passwordValue.length < 6) {
        passwordError.textContent = 'A senha tem que ter pelo menos 6 caracteres.';
        passwordInput.classList.add('invalid');
        isValid = false;
    }

    
    if (isValid) {
        alert('WAAAAAHHHH.');
        
    }
});

