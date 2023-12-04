
import os
import openai
from dotenv import load_dotenv
load_dotenv()

def generateCourse(transcript):
    token = os.getenv("API_KEY")
    openai.api_key = token
    prompt = f"Act like a evaluator, These are some of the questions with their taxonomy: 1. What do you remember about? - Remembering , 2. How would you define _______________? - Remembering , 3. How would you identify_________________? - Remembering , 4. How would you recognize ____________________? - Remembering , 5. What would you choose _______________? - Remembering , 6. Describe what happens when _________________? - Remembering , 7. How is (are) ________________? - Remembering , 8. Where is (are) ________________? - Remembering , 9. Which one ________________? - Remembering , 10. Who was _________________? - Remembering , 11. Why did _______________? - Remembering , 12. What is (are) __________________? - Remembering , 13. When did __________________? - Remembering , 14. How would you outline __________________? - Remembering , 15. List the __________________ in order. - Remembering , 16. How would you compare ____________? - Understanding , 17. How would you clarify the meaning ________________? - Understanding , 18. How would you differentiate between ____________________? - Understanding , 19. How would you generalize __________________? - Understanding , 20. How would you express ________________? - Understanding , 21. What can you infer from ____________________? - Understanding , 22. What did you observe ________________? - Understanding , 23. How would you identify __________________? - Understanding , 24. How can you describe _____________? - Understanding , 25. Will you restate ________________? - Understanding , 26. Elaborate on _____________. - Understanding , 27. What would happen if ________________? - Understanding , 28. What is the main idea of _________________? - Understanding , 29. What can you say about _______________? - Understanding , 30. What actions would you take to perform _________________? - Application , 31. How would you develop _____________ to present _______________? - Application , 32. What other way would you choose to _______________? - Application , 33. What would the result be if ________________? - Application , 34. How would you demonstrate ____________________? - Application , 35. How would you present _________________? - Application , 36. How would you change _________________? - Application , 37. How would you modify _____________? - Application , 38. How could you develop __________________? - Application , 39. Why does _______________ work? - Application , 40. How would you alter ____________ to ______________? - Application , 41. What examples can you find that ______________? - Application , 42. How would you solve _________________? - Application , 43. How can you classify _____________ according to ______________? - Analysis , 44. How can you compare the different parts _____________? - Analysis , 45. What explanation do you have for __________________? - Analysis , 46. How is _______________ connected to __________________? - Analysis , 47. Discuss the pros and cons of _________________. - Analysis , 48. How can you sort the parts ________________? - Analysis , 49. What is the analysis of _________________? - Analysis , 50. What can you infer _________________? - Analysis , 51. What ideas validate ______________________? - Analysis , 52. How would you explain ____________________? - Analysis , 53. What can you point out about ________________? - Analysis , 54. What is the problem with _____________? - Analysis , 55. Why do you think _____________? - Analysis , 56. What criteria would you use to assess _______________? - Evaluation-synthesis , 57. What data was used to evaluate ____________? - Evaluation-synthesis , 58. What choice would you have made _______________? - Evaluation-synthesis , 59. How would you determine the facts ______________? - Evaluation-synthesis , 60. What is the most important _____________? - Evaluation-synthesis , 61. What would you suggest ____________? - Evaluation-synthesis , 62. How would you grade ____________? - Evaluation-synthesis , 63. What is your opinion of ______________? - Evaluation-synthesis , 64. How could you verify ______________? - Evaluation-synthesis , 65. What information would you use to prioritize ________________? - Evaluation-synthesis , 66. Rate the ____________. - Evaluation-synthesis , 67. Rank the importance of ______________. - Evaluation-synthesis , 68. Determine the value of ______________ - Evaluation-synthesis , 69. What alternative would you suggest for ______________ - Creating-Synthesis , 70. What changes would you make to revise __________________ - Creating-Synthesis , 71. How would you explain the reason ______________ - Creating-Synthesis , 72. How would you generate a plan to ________________ - Creating-Synthesis , 73. What could you invent ______________ - Creating-Synthesis , 74. What facts can you gather ________________ - Creating-Synthesis , 75. Predict the outcome if _______________. - Creating-Synthesis , 76. What would happen if _________________ - Creating-Synthesis , 77. How would you portray ______________ - Creating-Synthesis , 78. Devise a way to _____________. - Creating-Synthesis , 79. How would you compile the facts for _____________ - Creating-Synthesis , 80. How would you elaborate on the reason ________________ - Creating-Synthesis , 81. How would you improve _____________ - Creating-Synthesis . Now based on these question tell me the taxonomy of the question: {transcript}"
    response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=10)
    print(response)  # "A long time ago in a galaxy far, far away."


generateCourse("Who was akbar?")