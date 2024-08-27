
# Strong Password - Hackerrank

This Python script solves the "Strong Password" problem by determining the minimum number of characters that need to be added to make a given password strong. A password is considered strong if it meets certain criteria related to length, and the presence of different types of characters.

https://www.hackerrank.com/challenges/strong-password/problem

## Implementation

The minimumNumber function checks each character in the password to see if it meets any of the required criteria (digit, lowercase, uppercase, special character). It then calculates the number of missing character types and the number of characters needed to reach the minimum length of 6.

### Explanation

1. **Checking Character Types**:
   - The function uses boolean flags (has_digit, has_lower, has_upper, has_special) to check if each type of character is present in the password.

2. **Counting Missing Types**:
   - It counts how many of the required character types are missing.

3. **Using the max() Function**:
   - The max() function determines whether the number of missing character types or the number needed to reach 6 characters is greater, ensuring the password meets all requirements.

