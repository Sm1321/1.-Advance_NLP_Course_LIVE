from setuptools import find_packages,setup



setup(name = "Agentic-Trading-Bot",
      version = "0.0.1",
      author = "Mohan",
      author_email = "siddulamohan1321@gmail.com",
      packages = find_packages(),
      install_requries = ['lancedb','langchain','langgraph','tavily-python','polygon']     
        )
