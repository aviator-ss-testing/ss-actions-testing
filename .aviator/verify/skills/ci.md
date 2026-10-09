# Driving the CI preview

The preview is a small static site with a sign-in gate for account pages.

## Signing in

Every scenario should sign in first:

1. Navigate to `/login` on the preview URL.
2. Fill the email field with `tester@example.com`.
3. Fill the password field with `{{ secrets.E2E_PASSWORD }}`.
4. Click "Sign in". A successful sign-in lands on `/account`, which shows "Signed in as tester@example.com".

## Where things live

- `/status.html` is the public status page (no sign-in needed).
- `/account` is the signed-in account page.
