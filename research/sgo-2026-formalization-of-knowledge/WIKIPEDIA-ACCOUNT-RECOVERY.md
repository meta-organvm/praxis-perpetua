# Wikipedia Account Recovery — Apadavano

## Status: Account Locked (Anti-Bruteforce)

**Date:** 2026-03-23
**Cause:** Multiple API authentication attempts during SGO research session triggered Wikipedia's rate limiting and account lockout.

## Recovery Steps

1. **Wait 24 hours** from the last failed attempt (2026-03-23). The lockout typically expires automatically.

2. **Go to:** https://en.wikipedia.org/wiki/Special:PasswordReset
   - Enter username: `Apadavano`
   - Request password reset email
   - Follow the email link to set a new password

3. **If the email doesn't arrive:** Check the email associated with the account (registered 2020-11-14). If the email is no longer accessible, contact Wikipedia support via https://en.wikipedia.org/wiki/Special:Contact

4. **After recovery:** Change the password to something strong and DIFFERENT from anything that appeared in this conversation session.

## Lesson Learned

Do not authenticate via API more than 2x in a single session. Each login attempt is logged. Multiple rapid attempts trigger progressive lockout. For future sessions: authenticate ONCE, reuse the cookies, clean up at end.

## IRF Reference

This is tracked as a follow-up item. The old password `Padavano!8` was exposed in conversation — regardless of lockout, it MUST be changed upon recovery.
