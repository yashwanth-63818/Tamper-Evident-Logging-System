Tamper Evident Logging System

This system records logs in a secure way using SHA256 hashing.
Each log entry stores the hash of the previous log entry.

If any log is modified or deleted, the system detects tampering
when the verification function is executed.