class Cryptographie:
    def __init__(self, qcm1_score, qcm1_weight, qcm2_score, qcm2_weight, cc_score, cc_weight):
        self.qcm1_score = qcm1_score
        self.qcm1_weight = qcm1_weight
        self.qcm2_score = qcm2_score
        self.qcm2_weight = qcm2_weight
        self.cc_score = cc_score
        self.cc_weight = cc_weight
        self.final_weight = 1 - (qcm1_weight + qcm2_weight + cc_weight)

    def calculate_needed_final_score(self, pass_score=10):
        # Calculate current weighted score
        current_score = (
                (self.qcm1_score * self.qcm1_weight) +
                (self.qcm2_score * self.qcm2_weight) +
                (self.cc_score * self.cc_weight)
        )
        # Calculate the score needed in the final
        needed_score = (pass_score - current_score) / self.final_weight
        return max(0, needed_score)  # Ensure no negative scores


# Input values for the Cryptography class
cryptography = Cryptographie(
    qcm1_score=19.17,
    qcm1_weight=0.1,
    qcm2_score=15.75,
    qcm2_weight=0.1,
    cc_score=9.5,
    cc_weight=0.3
)

needed_score = cryptography.calculate_needed_final_score()
print(needed_score)


class Algorithms:
    def __init__(self, cc1_score, cc1_weight, cc2_score, cc2_weight):
        self.cc1_score = cc1_score
        self.cc1_weight = cc1_weight
        self.cc2_score = cc2_score
        self.cc2_weight = cc2_weight
        self.final_weight = 1 - (cc1_weight + cc2_weight)

    def calculate_needed_final_score(self, pass_score=10):
        # Calculate current weighted score
        current_score = (
                (self.cc1_score * self.cc1_weight) +
                (self.cc2_score * self.cc2_weight)
        )
        # Calculate the score needed in the final
        needed_score = (pass_score - current_score) / self.final_weight
        return max(0, needed_score)  # Ensure no negative scores


# Input values for the Algorithms class
algorithms = Algorithms(
    cc1_score=15,
    cc1_weight=0.25,
    cc2_score=12.5,
    cc2_weight=0.25
)

needed_score_algorithms = algorithms.calculate_needed_final_score()
print(needed_score_algorithms)


class Automata:
    def __init__(self, cc_score, cc_weight, qcm_score, qcm_weight):
        self.cc_score = cc_score
        self.cc_weight = cc_weight
        self.qcm_score = qcm_score
        self.qcm_weight = qcm_weight
        self.final_weight = 1 - (cc_weight + qcm_weight)

    def calculate_needed_final_score(self, pass_score=10):
        # Calculate current weighted score
        current_score = (
                (self.cc_score * self.cc_weight) +
                (self.qcm_score * self.qcm_weight)
        )
        # Calculate the score needed in the final
        needed_score = (pass_score - current_score) / self.final_weight
        return max(0, needed_score)  # Ensure no negative scores


# Input values for the Automata class
automata = Automata(
    cc_score=16.5,
    cc_weight=0.3,
    qcm_score=19,
    qcm_weight=0.2
)

needed_score_automata = automata.calculate_needed_final_score()
print(needed_score_automata)


class PCOO:
    def __init__(self, cc_score, cc_weight, project_score, project_weight):
        self.cc_score = cc_score
        self.cc_weight = cc_weight
        self.project_score = project_score
        self.project_weight = project_weight
        self.final_weight = 1 - (cc_weight + project_weight)

    def calculate_needed_final_score(self, pass_score=10):
        # Calculate current weighted score
        current_score = (
                (self.cc_score * self.cc_weight) +
                (self.project_score * self.project_weight)
        )
        # Calculate the score needed in the final
        needed_score = (pass_score - current_score) / self.final_weight
        return max(0, needed_score)  # Ensure no negative scores


# Input values for the PCOO class
pcoo = PCOO(
    cc_score=20,
    cc_weight=0.25,
    project_score=10,
    project_weight=0.25
)

needed_score_pcoo = pcoo.calculate_needed_final_score()
print(needed_score_pcoo)
