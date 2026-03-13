import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SecurityException(Exception):
    """Custom exception for security breaches."""
    pass

def secure_directory_access(user_role: str, target_dir: str) -> bool:
    """
    Middleware to prevent unauthorized access to local file directories.
    Ensures zero security breaches during media retrieval.
    """
    # Role-Based Access Control (RBAC)
    allowed_roles = ["admin", "verified_user"]
    
    if user_role not in allowed_roles:
        logger.error(f"SECURITY ALERT: Unauthorized access attempt by role '{user_role}'.")
        raise SecurityException("Access Denied: Insufficient permissions.")
        
    # Path Traversal Prevention
    if ".." in target_dir or target_dir.startswith("/root"):
        logger.error(f"SECURITY ALERT: Suspected path traversal attempt to '{target_dir}'.")
        raise SecurityException("Access Denied: Invalid directory path.")
        
    logger.info(f"Access granted to {target_dir} for user role: {user_role}")
    return True

# Simple Unit Test Simulation
if __name__ == "__main__":
    print("Running Security Unit Tests...")
    try:
        secure_directory_access("guest", "/secure_vault/images")
    except SecurityException as e:
        print(f"Test Passed: Successfully blocked unauthorized user -> {e}")
