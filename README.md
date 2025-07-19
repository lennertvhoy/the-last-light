# The Last Light: A Book Project

This repository contains the manuscript for "The Last Light," a book exploring the intersection of consciousness, artificial intelligence, and the future of humanity, heavily inspired by the works of Peter Watts.

## Project Structure

-   `README.md`: This file.
-   `00-introduction/`: The book's introduction.
-   `01-the-chinese-room/`: Section on AI, consciousness, and the "Chinese Room" thought experiment.
-   `02-layer-8-singularity/`: Section on the societal-scale impacts of AI.
-   `03-the-digital-pathogen/`: Section on information warfare and cognitive security.
-   `04-vampires-and-bicamerals/`: Section connecting vampiric predation to cognitive science.
-   `05-weaponized-consciousness/`: Section on the strategic value of self-awareness.
-   `06-the-oppenheimer-moment/`: Section on the ethical and existential risks.
-   `07-echopraxia/`: Section on the biological path to post-humanism.
-   `08-the-dead-end/`: Section on civilizational collapse scenarios.
-   `09-or-a-new-beginning/`: A look at potential positive futures.
-   `10-appendices/`: Appendices with supplementary material.
-   `11-scripts/`: Contains utility scripts for project management.
-   `12-summary/`: Contains summaries of the book.

## How to Use

### Combining the Book

To compile all individual markdown files into a single manuscript, use the provided scripts. They automatically find all chapters in the numbered directories and combine them in the correct order. The output is saved in a `_build` directory at the project root.

### For Windows (PowerShell)

1.  Open a PowerShell terminal in the project root.
2.  Run the command: `.\11-scripts\combine-book.ps1`

### For macOS/Linux (Bash)

1.  Open a terminal in the project root.
2.  Make the script executable: `chmod +x ./11-scripts/combine-book.sh`
3.  Run the command: `./11-scripts/combine-book.sh`

### Generating an Audiobook

The `/11-scripts/audiobook-converter` directory contains a web-based tool to convert markdown files into audiobooks using various Text-to-Speech (TTS) providers.

1.  Open the `index.html` file in that directory in a modern web browser.
2.  Follow the on-screen instructions to select a TTS provider, enter your API key, and upload a markdown file (such as the combined book file).
3.  For more details, see the `README.md` file within the `audiobook-converter` directory.
## Contributing

Contributions to this project are welcome. The book is structured as a collection of markdown files in numbered directories, which represent the parts and chapters.

### Editing in VS Code

1.  **Open the project** in Visual Studio Code.
2.  **Find the chapter** you wish to edit in the corresponding numbered directory.
3.  **Open the markdown file**.
4.  To see a live preview of your changes, use the split-screen feature:
    *   Click the **"Split Editor Right"** button in the top-right corner of the editor tab bar.
    *   In the new editor pane, click the **"Open Preview"** button (magnifying glass icon).
5.  You can now edit the markdown text in the left pane and see the formatted preview update live in the right pane.

### Submitting Changes

Please follow standard GitHub workflow for submitting contributions:

1.  Fork the repository.
2.  Create a new branch for your feature or fix.
3.  Commit your changes.
4.  Push to your fork and submit a pull request.