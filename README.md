# email-slicer

# Step 1: Collect User Input
- Use the input() function to prompt the user to enter an email address. This function retrieves user input as a string.

# Step 2: Validate the Email Address
- Before splitting the email address, validate its format:

- Ensure the presence of "@" character using the in operator or .find() method.
- Verify the presence of at least one dot "." in the domain part of the email address.

# Step 3: Split the Email Address
- Use string manipulation techniques to split the email address into two parts:
-Username: Extract the substring before the "@" symbol. This can be achieved using slicing or methods like .split() or .index().
- Domain: Extract the substring after the "@" symbol. Again, slicing or methods like .split() or .index() can be used.
# Step 4: Display the Results
- Once the email address is successfully split into username and domain parts, display these parts in a readable format to the user.

# Step 5: Repeat the Process or Terminate
- Provide the user with options to either process another email address or terminate the program. This can be implemented using loops and conditional statements.

# Step 6: Error Handling
- Implement additional checks to handle potential errors:

- Check if the "@" symbol is present in the email address.
- Validate the format of the email address to avoid incorrect inputs.
- Handle cases with extra spaces or incorrect formatting gracefully.
# Conclusion

Following these steps allows you to create an "Email Slicer" program in Python. This program will prompt the user for an email address, validate its format, split it into username and domain parts, display the results, and provide options for further processing or terminating the program.

# Methods Used:
.split(): Splits a string into a list based on a delimiter.
.index(): Finds the index of a substring within a string.
Slicing: Extracts substrings based on indices.
String manipulation: Techniques to modify or extract parts of strings.
By utilizing these methods and techniques effectively, you can create a robust and user-friendly Email Slicer program in Python.
