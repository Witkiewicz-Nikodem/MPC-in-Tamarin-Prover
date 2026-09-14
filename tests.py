import subprocess
import re
import sys


def run_test(model):
    command = [
        "tamarin-prover",
        model,
        "--prove"
    ]

    result = subprocess.run(
        ["/usr/bin/time", "-v"] + command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    stdout_lines = result.stdout.splitlines()

    start_index = None
    for i, line in enumerate(stdout_lines):
        if "processing time:" in line:
            start_index = i
            break

    if start_index is not None:
        for line in stdout_lines[start_index:]:
            print(line)
    else:
        print("'processing time:' not found.")
        print(result.stdout)

    print("=" * 80)
    print("TIME / RESOURCE USAGE REPORT")
    print("=" * 80)

    match = re.search(
        r"(Command being timed:.*?Exit status:.*)",
        result.stderr,
        re.DOTALL,
    )

    if match:
        print(match.group(1))
    else:
        print("Nie znaleziono raportu /usr/bin/time.")

    print("=" * 80)
    print("TAMARIN RESULT")
    print("=" * 80)

    print("=" * 80)
    print(f"EXIT CODE: {result.returncode}")
    print("=" * 80)

models = [
    "./complexity_measures/2_party/MPC.spthy",
    "./complexity_measures/3_party/MPC.spthy",
    "./complexity_measures/4_party/MPC.spthy",
    "./semi_honest/MPC.spthy",
    "./GOD/MPC.spthy",
    "./fairness/MPC.spthy",
    "./sec_with_abort/MPC.spthy",
    ]


if len(sys.argv) == 1:
    for model in models:
        run_test(model)
else:
    option = sys.argv[1]
    if   option == "C2":
        run_test(models[0])
    elif option == "C3":
        run_test(models[1])
    elif option == "C4":
        run_test(models[2])
    elif option == "AllC":
        for model in models[0:3]:
            run_test(model)
    elif option == "semi-honest":
        run_test(models[4])     
    elif option == "GOD":
        run_test(models[4])
    elif option == "Fairness":
        run_test(models[5])
    elif option == "Abort":
        run_test(models[6])

    else:
        print("wrong argument, no model found")