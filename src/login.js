function validateLoginForm(username, password) {
  return username.trim().length > 0 && password.length > 0;
}

function updateLoginButton(usernameInput, passwordInput, submitButton) {
  const isValid = validateLoginForm(usernameInput.value, passwordInput.value);
  submitButton.disabled = !isValid;
}

function initLoginForm() {
  const usernameInput = document.getElementById('username');
  const passwordInput = document.getElementById('password');
  const submitButton = document.getElementById('login-btn');

  submitButton.disabled = true;

  usernameInput.addEventListener('input', () => {
    updateLoginButton(usernameInput, passwordInput, submitButton);
  });

  passwordInput.addEventListener('input', () => {
    updateLoginButton(usernameInput, passwordInput, submitButton);
  });
}

document.addEventListener('DOMContentLoaded', initLoginForm);
