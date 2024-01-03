<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/bkenks/PDFChat">
    <h1>:page_facing_up:</h1>
  </a>

<h3 align="center">PDFChat</h3>

  <p align="center">
    PDFChat is an application built to "chat" with private data, such as a PDF. Develoment will continue to add support for other types of data.
    ·
    <a href="https://github.com/bkenks/PDFChat/issues">Report Bug</a>
    ·
    <a href="https://github.com/bkenks/PDFChat/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://i.imgur.com/RaZuEnb.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 3.11
    + Install from [Python.org](https://www.python.org/)
* Faiss-CPU
* LangChain
* InstructorEmbedding
* PyPDF2
* TikToken
* Sentence_Transformers

### Installation (Windows)

1. Clone the repo
   ```sh
   git clone https://github.com/bkenks/PDFChat
   ```
2. Create Python 3.11 Virtual Environment
   ```sh
   py -3.11 -m venv .venv
   ```
3. Activate virtual environment
  ```sh
  .venv/Scripts/Activate
  ```
4. Install packages
   ```sh
   pip install -r requirements.txt
   ```
5. Get an OpenAI API Key at [OpenAI.com](https://openai.com/)
6. Enter your API in a new file in the working directory called `.env`
   ```sh
   OPENAI_API_KEY = 'ENTER YOUR API';
   ```
7. Run program
   ```sh
   streamlit run main.py
   ```
8. Program should open in your browser automatically

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Brian Kenkel - [LinkedIn](linkedin-url)

Project Link: [https://github.com/bkenks/PDFChat](https://github.com/bkenks/PDFChat)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/bkenks/PDFChat.svg?style=for-the-badge
[contributors-url]: https://github.com/bkenks/PDFChat/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/bkenks/PDFChat.svg?style=for-the-badge
[forks-url]: https://github.com/bkenks/PDFChat/network/members
[stars-shield]: https://img.shields.io/github/stars/bkenks/PDFChat.svg?style=for-the-badge
[stars-url]: https://github.com/bkenks/PDFChat/stargazers
[issues-shield]: https://img.shields.io/github/issues/bkenks/PDFChat.svg?style=for-the-badge
[issues-url]: https://github.com/bkenks/PDFChat/issues
[license-shield]: https://img.shields.io/github/license/bkenks/PDFChat.svg?style=for-the-badge
[license-url]: https://github.com/bkenks/PDFChat/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/briankenkel/
[product-screenshot]: images/screenshot.png
