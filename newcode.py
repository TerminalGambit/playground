import pandas as pd


def load_data():
    data = {
        "Identifiant": [
            22413409, 22300172, 21903989, 22311937, 21707517, 22410777, 22410771, 22411295, 22310114, 22410883,
            21901111, 22305456, 410743, 22412141, 22211287, 22301162, 22311016, 22302506, 22104520, 22302406,
            22409899, 22302612, 22306981, 2240561, 22413790, 22410451, 21602528, 22201416, 22410856, 22311101,
            22018441, 22302558, 22102365, 22202611, 21808599, 22003839, 22410754, 22111424, 21707296, 2211142,
            22200336, 22411663, 22407008, 22311033, 22311038, 22102516, 21702841, 22310098, 22204830, 22113606,
            410777, 305480, 22101956, 22310956, 22208976, 21908724, 22306131, 21704226, 22012565, 22207560,
            22310984, 22301827, 22410743, 22201315, 22410747, 22206581, 22201239, 22100086, 22309458, 22410739,
            22309804, 22205857, 412141, 22000383, 22310466, 22304346, 22411704, 22208430, 22302280, 22205757,
            22109373, 21909073, 22108888, 22116709, 22100496, 22309309, 22102678, 22200641, 22305480, 22304823,
            21902961, 22103841, 22405621
        ],
        "Moyenne": [
            13.12, 13.62, 5.75, 16.62, 5.33, 12.40, 15.37, 16.00, 10.33, 10.25,
            11.60, 16.25, 12.00, 2.00, 11.87, 14.12, 11.12, 0, 7.33, 0,
            18.33, 15.20, 11.00, 12.00, 10.50, 19.00, 19.62, 19.25, 18.40, 10.16,
            8.25, 8.50, 13.75, 19.00, 19.50, 12.00, 17.37, 11.33, 14.37, 7.00,
            15.75, 10.25, 8.37, 0, 10.16, 16.37, 8.66, 19.50, 18.00, 5.50,
            13.00, 6.00, 0, 13.62, 13.75, 1.66, 0, 13.50, 14.87, 19.37,
            11.75, 12.75, 17.80, 16.00, 19.25, 16.12, 14.50, 12.75, 13.87, 13.37,
            14.00, 19.00, 10.00, 10.83, 11.00, 17.83, 8.12, 16.00, 9.62, 0.66,
            7.33, 11.20, 0, 19.87, 13.66, 16.62, 10.33, 19.75, 13.40, 8.16,
            10.16, 8.00, 13.00
        ]
    }
    return pd.DataFrame(data)


def analyze_data(df):
    mean_grade = df["Moyenne"].mean()
    best_student = df.loc[df["Moyenne"].idxmax()]
    return mean_grade, best_student


def find_grade_by_id(df, student_id):
    result = df.loc[df["Identifiant"] == student_id, "Moyenne"]
    return result.iloc[0] if not result.empty else None


def get_ranking_by_id(df, student_id):
    df_sorted = df.sort_values(by="Moyenne", ascending=False).reset_index(drop=True)
    ranking = df_sorted[df_sorted["Identifiant"] == student_id].index.values
    return ranking[0] + 1 if ranking.size > 0 else None


if __name__ == "__main__":
    df = load_data()
    mean, best = analyze_data(df)
    student_id = 22207560
    student_grade = find_grade_by_id(df, student_id)
    student_rank = get_ranking_by_id(df, student_id)

    print(f"Mean Grade: {mean:.2f}")
    print(f"Best Grade: {best['Moyenne']:.2f}, ID: {best['Identifiant']}")
    print(f"Grade for ID {student_id}: {student_grade}")
    print(f"Ranking for ID {student_id}: {student_rank}")
