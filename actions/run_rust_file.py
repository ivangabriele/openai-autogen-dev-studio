import subprocess

from constants import PROJECT_DIRECTORY_PATH


def run_rust_file(rust_file_path: str) -> str:
    """
    Compiles and runs a Rust source file.
    Assumes that `rustc` is installed and available in `PATH`.
    Returns the output of the Rust program.
    """
    # Compile the Rust code
    compile_command = ["rustc", rust_file_path, "-o", "temp_executable"]
    try:
        subprocess.check_call(compile_command, cwd=PROJECT_DIRECTORY_PATH)
    except subprocess.CalledProcessError:
        return "Error compiling Rust code."

    # Run the compiled Rust code
    run_command = ["./temp_executable"]
    try:
        output = subprocess.check_output(
            run_command, cwd=PROJECT_DIRECTORY_PATH, stderr=subprocess.STDOUT
        )
        return output.decode("utf-8")
    except subprocess.CalledProcessError as error:
        return f"Error running Rust code: {error.output.decode('utf-8')}"
    finally:
        # Clean up the temporary executable
        subprocess.call(["rm", "temp_executable"])
