def extract_chain():

    class MockExtract:

        def invoke(self, input):

            return {
                "skills": ["python", "machine learning"],
                "tools": ["git", "docker"],
                "experience": "2 years"
            }

    return MockExtract()