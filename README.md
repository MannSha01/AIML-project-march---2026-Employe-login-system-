# AIML-project ~ Employee Login System
- A Python-based CAPTCHA verification system with Tkinter GUI and speech accessibility using pyttsx3.
- This project demonstrates how to integrate image-based CAPTCHA with voice feedback for enhanced usability and security in an employee login workflow.



 **Features**
- Random CAPTCHA generation (letters + digits).
- Noise and distortion (lines, dots, random colors) for security.
- Tkinter GUI for user interaction.
- Speech feedback using pyttsx3:
- Reads out CAPTCHA characters.
- Confirms typed input.
- Announces success/failure.
- Credential check (requires Name and Office ID before verification).
- Double-enter confirmation to reduce accidental submissions.
- Fail counter with automatic CAPTCHA refresh.


**Requirements**
**(Libraries requried:)**
- Pillow → CAPTCHA image generation.
- pyttsx3 → Text-to-speech engine for voice prompts.
- Tkinter → GUI framework.
- random, string, _thread → Logic and threading support.
- Open cmd prompt and bash pip install pillow
- Open cmd prompt and bash pip install pyttsx3
- other linraries are genereally pre installed with python 
- Python version: 3.8+


**How to Run**
- Save the script as employee_login_system.py.
- Run the program:
- python employee_login_system.py
- Enter your Name and Office ID.
- Type the CAPTCHA shown in the image box:
- Press Enter once → system reads your input aloud.
- Press Enter again → system verifies against the CAPTCHA.


**Use buttons:**
- Verify → manually trigger verification.
- Refresh CAP → generate a new CAPTCHA.
- Speak CAPTCHA → hear the CAPTCHA characters read aloud.
- Usage Flow
- User enters credentials (Name + Office ID).
- CAPTCHA image is generated with random characters.
- User types the CAPTCHA in the input box.
- System provides voice confirmation and requires a second Enter press.
- Verification result:
- Success → "Captcha verified" + welcome message.
- Failure → "Captcha failed" + new CAPTCHA generated.



**Security Notes**
- CAPTCHA uses randomized characters, colors, lines, and noise to prevent automated recognition.
- Double-enter confirmation reduces accidental submissions.


**Accessibility**
- Voice prompts guide the user through the process.
- CAPTCHA characters are read aloud for visually impaired users.
- Error messages are both visual (labels) and spoken.



**Future Improvements**
- Audio CAPTCHA option: Generate spoken CAPTCHA codes for users who cannot see the screen.
- Database integration: Store and validate employee credentials against a secure database.
- Stronger CAPTCHA distortion: Add curves, warping, and background textures for higher security.
- Multi-language support: Provide speech prompts in different languages.
- Adaptive difficulty: Increase CAPTCHA complexity after repeated failures.
- Logging system: Track login attempts, failures, and timestamps for auditing.
- GUI enhancements: Modernize interface with better styling and responsive layout.
- Threading improvements: Optimize speech engine handling to avoid blocking during GUI updates.


