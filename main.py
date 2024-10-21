def complex_add(a, b):

    """Add two complex numbers."""

    return (a[0] + b[0], a[1] + b[1])  # (real, imaginary)



def complex_sub(a, b):

    """Subtract two complex numbers."""

    return (a[0] - b[0], a[1] - b[1])  # (real, imaginary)



def complex_mul(a, b):

    """Multiply two complex numbers."""

    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])  # (real, imaginary)



def complex_exp(theta):

    """Calculate e^(i * theta) for a given angle theta."""

    return (cos(theta), sin(theta))



def cos(theta):

    """Calculate cosine of theta."""

    return sum((-1)**n * (theta**(2*n)) / factorial(2*n) for n in range(10))  # Taylor series approximation



def sin(theta):

    """Calculate sine of theta."""

    return sum((-1)**n * (theta**(2*n + 1)) / factorial(2*n + 1) for n in range(10))  # Taylor series approximation



def factorial(n):

    """Calculate factorial of n."""

    if n == 0:

        return 1

    result = 1

    for i in range(1, n + 1):

        result *= i

    return result



def fft(x):

    """Compute the Fast Fourier Transform of a sequence."""

    N = len(x)

    if N <= 1:

        return x



    # Divide the input into even and odd parts

    even = fft(x[0::2])  # FFT of even-indexed elements

    odd = fft(x[1::2])   # FFT of odd-indexed elements



    # Combine the results

    return combine(even, odd)



def combine(even, odd):

    """Combine the results of the FFT of even and odd indexed elements."""

    N = len(even) + len(odd)

    result = [None] * N

    for k in range(len(odd)):

        theta = -2 * 3.141592653589793 * k / N  # Calculate angle

        w = complex_exp(theta)  # e^(i * theta)

        result[k] = complex_add(even[k], complex_mul(w, odd[k]))

        result[k + len(odd)] = complex_sub(even[k], complex_mul(w, odd[k]))

    return result



def compute_fft(input_sequence):

    """Compute the FFT of the input sequence and return the result."""

    # Convert input sequence to complex numbers

    x = [(num, 0) for num in input_sequence]  # Represent as (real, imaginary)

    return fft(x)



def main():

    """Main function to run the FFT calculator."""

    # Sample input: a simple sequence

    x = [0, 1, 2, 3, 4, 5, 6, 7]  # Length should be a power of 2

    print("Input sequence:", x)

    

    # Calculate FFT

    fft_result = compute_fft(x)

    print("FFT result:", fft_result)



if __name__ == "__main__":

    main()



