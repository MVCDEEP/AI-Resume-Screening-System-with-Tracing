def score_chain():

    class MockScore:

        def invoke(self, input):

            return {
                "score": 78,
                "explanation": "Candidate matches most required skills."
            }

    return MockScore()