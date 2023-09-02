
# OCR-Text-Analysis

This project describes a self-developed endeavor focused on Optical Character Recognition (OCR) and text analysis. In this project, we aim to perform text extraction from visual data and simultaneously identify sensitive data types within the extracted text. The project utilizes various techniques to identify specific sensitive data types and incorporates caching for reprocessing the same image.

## Project Features

- **API Endpoint Format:** The API adheres to a specific response format.

- **HTTP Methods:** The API endpoint uses the POST HTTP method for image submission.

- **Text Extraction:** Efficiently performs text extraction from images.

- **Sensitive Data Verification:** Implements algorithms to verify sensitive data found in the extracted text.

- **Project Report:** After project completion, a comprehensive report summarizes research, methodologies, and findings.

- **Deployment:** Deploy the project using tunneling mechanisms like ngrok or host it on a server, sharing an accessible URL.

## Expected HTTP Status Codes

- **HTTP 200 - Successful:** The operation was successful, and valid data was extracted.

- **HTTP 204 - No Content:** The image was processed, but no text or sensitive data was found.

- **HTTP 400 - Bad Request:** The image couldn't be processed, or it was in an unsupported format.

  
## Sensitive Data Types to Extract

- PHONE_NUMBER
- ID_NUMBER
- CREDIT_CARD_NUMBER
- PLATE
- DATE
- EMAIL
- DOMAIN
- URL
- HASH
- COMBOLIST
- 
## Technologies Used

- Python 3.11
- FastAPI
- Docker Compose
- Poetry
- Redis (for caching)

## How to Use

- Open a terminal in the project's root directory.
- Install the required dependencies first:

   ```bash
   poetry install
   docker-compose build
   docker-compose up -d
- Run the FastAPI server:
  or go to the src/api directory and run the following command
  ```bash
   poetry run uvicorn api:app --host 0.0.0.0 --port 8000
- Access http://localhost:8000 in your browser or API testing tools.

## Conclusion

In conclusion, this project has successfully addressed the challenges of Optical Character Recognition (OCR) and text analysis, focusing on the extraction of valuable information from images and the identification of sensitive data types within that text. The project aimed to enhance the efficiency and accuracy of data extraction and analysis while providing a caching mechanism for improved performance.

