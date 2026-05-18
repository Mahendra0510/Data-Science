import numpy as np

# ------------------------------------------
# 1. Generate Random Scores
# ------------------------------------------

# Generate 50 random student scores (0–100)
scores = np.random.randint(0, 100, size=50)

print("===== STUDENT SCORES =====")
print(scores)

# ------------------------------------------
# 2. Basic Statistics
# ------------------------------------------

mean_score = np.mean(scores)
median_score = np.median(scores)
highest_score = np.max(scores)
lowest_score = np.min(scores)
std_deviation = np.std(scores)

# Percentiles
percentile_25 = np.percentile(scores, 25)
percentile_75 = np.percentile(scores, 75)

print("\n===== STATISTICS =====")
print(f"Mean Score      : {mean_score:.2f}")
print(f"Median Score    : {median_score}")
print(f"Highest Score   : {highest_score}")
print(f"Lowest Score    : {lowest_score}")
print(f"Standard Dev.   : {std_deviation:.2f}")
print(f"25th Percentile : {percentile_25}")
print(f"75th Percentile : {percentile_75}")

# ------------------------------------------
# 3. Find Failures and Distinctions
# ------------------------------------------

# Students scoring below 40
fail_scores = scores[scores < 40]

# Students scoring above 85
distinction_scores = scores[scores > 85]

print("\n===== FAILING STUDENTS (<40) =====")
print(fail_scores)

print("\n===== DISTINCTION STUDENTS (>85) =====")
print(distinction_scores)

# ------------------------------------------
# 4. Normalize Scores (0 to 1)
# ------------------------------------------

normalized_scores = (
    (scores - np.min(scores)) /
    (np.max(scores) - np.min(scores))
)

print("\n===== NORMALIZED SCORES =====")
print(normalized_scores)

# ------------------------------------------
# 5. Reshape into 5 x 10 Matrix
# ------------------------------------------

# Assume:
# 5 subjects
# 10 students per subject

score_matrix = scores.reshape(5, 10)

print("\n===== SCORE MATRIX (5 x 10) =====")
print(score_matrix)

# ------------------------------------------
# 6. Compute Row-wise Averages
# ------------------------------------------

subject_averages = np.mean(score_matrix, axis=1)

print("\n===== SUBJECT-WISE AVERAGES =====")
for i, avg in enumerate(subject_averages, start=1):
    print(f"Subject {i} Average: {avg:.2f}")

# ------------------------------------------
# 7. Bonus Challenge
# Weighted Final Scores
# ------------------------------------------

# Generate theory and practical scores
theory_scores = np.random.randint(0, 100, size=50)
practical_scores = np.random.randint(0, 100, size=50)

# Weightage:
# Theory = 40%
# Practical = 60%

final_scores = (
    (0.4 * theory_scores) +
    (0.6 * practical_scores)
)

print("\n===== THEORY SCORES =====")
print(theory_scores)

print("\n===== PRACTICAL SCORES =====")
print(practical_scores)

print("\n===== WEIGHTED FINAL SCORES =====")
print(final_scores)

# ------------------------------------------
# 8. Topper Information
# ------------------------------------------

topper_score = np.max(scores)
topper_index = np.argmax(scores)

print("\n===== TOPPER DETAILS =====")
print(f"Topper Score : {topper_score}")
print(f"Student Index: {topper_index}") 