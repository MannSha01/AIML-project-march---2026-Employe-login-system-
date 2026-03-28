# Statement of Purpose – Employee Login System
 **Objective** ~
The Employee Login System is designed to demonstrate a secure and accessible login workflow using CAPTCHA verification combined with voice feedback.
Its primary goal is to prevent unauthorized access while ensuring usability for all employees, including those with visual impairments.

  **Scope**
- Provides a GUI-based login interface using Tkinter.
- Requires employees to input Name and Office ID before verification.
- Integrates CAPTCHA validation with randomized characters and distortion.
- Offers speech-based guidance to enhance accessibility.
- Tracks failed attempts and refreshes CAPTCHA automatically.

**Technical Highlights**
- Python 3.8+ implementation.
- Libraries used:
- Pillow → CAPTCHA image generation.
- pyttsx3 → Text-to-speech engine for voice prompts.
- Tkinter → GUI framework.
- random, string, _thread → Logic and threading support.
- Double-enter confirmation ensures deliberate input submission.
- Fail counter (tally_of_fails) improves security monitoring.

 **Security Considerations**
- CAPTCHA includes noise, random colors, and distortion to resist automated recognition.
- Requires employee credentials before verification.
- Tracks failed attempts to detect suspicious activity.

**Accessibility Commitment**
- Voice prompts guide users through every step.
- CAPTCHA characters are read aloud for visually impaired employees.
- Error messages are both spoken and displayed visually.

**Future Directions**
- Integration with employee databases for credential validation.
- Audio-only CAPTCHA for enhanced accessibility.
- Multi-language support for diverse workplaces.
- Adaptive CAPTCHA difficulty based on failure count.
- Logging and reporting system for audit trails.

**Statement**
This project is intended for educational and demonstration purposes.
It showcases how security and accessibility can be merged in a login system.
Organizations may adapt and extend this framework to build more robust, production-ready employee authentication solutions.
