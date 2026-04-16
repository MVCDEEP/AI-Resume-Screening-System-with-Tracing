def match_chain():

    class MockMatch:

        def invoke(self, input):

            return {
                "matched_skills": ["python"],
                "missing_skills": ["deep learning"]
            }

    return MockMatch()