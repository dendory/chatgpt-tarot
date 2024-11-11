## ChatGPT-Tarot

This is the code behind http://tarot.dendory.net

The files here can be used to create a simple ChatGPT powered static website. It contains 2 parts:

* The script in `script` can be used to select random cards, then get a reading from ChatGPT and populate the readings.json file.
* The static HTML files in `html` can be placed on any public web site, even an S3 bucket, and it will pick a random entry from the JSON file and present it to the viewer. It also contains a number of JPEG files for the cards. Those were created by myself using the Midjourney AI.

Note: Before you can use the script, you need to get your own ChatGPT API key from the OpenAI website and add it in the `get_readings.py` file.


## Screenshot

![Screenshot of the website](screenshot.png)


## License

Copyright 2024 Patrick Lambert

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

