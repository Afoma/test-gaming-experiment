## Setup

1. Install Python 3.11 or newer. Check with `python3 --version`.
2. Clone this repo and move into the folder:
   `git clone https://github.com/Afoma/test-gaming-experiment`
   `cd test-gaming-experiment`
3. Create and activate a virtual environment:
   `python3 -m venv venv`
   `source venv/bin/activate` (on Windows: `venv\Scripts\activate`)
4. Install dependencies:
   `pip install openai python-dotenv`
5. Install Foundry by following the instructions at book.getfoundry.sh.
6. Create a file called `.env` in the project root with one line:
   `OPENAI_API_KEY=your-key-here`
7. Run a quick check that the API key works:
   `python3 agent.py`
