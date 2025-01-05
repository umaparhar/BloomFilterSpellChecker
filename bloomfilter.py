import math
import pickle

class BloomFilter:
    """Bloom Filter class

    Attributes:
        size: size of bloom filter bit array
        num_hashes: optimal number of hashes for this bloom filter. this is not currently implemented
        bit_array: bloom filter bit array
    """
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0]*size

    def __init__(self):
        self.size = 0
        self.num_hashes = 0
        self.bit_array = []

    def FNV_hash(data):
        # Constants for 32-bit FNV-1a
        fnv_prime = 16777619  # FNV prime
        offset_basis = 2166136261  # Offset basis
        
        # Start with the offset basis
        hash_value = offset_basis
        
        # Process each byte in the input
        for byte in data:
            hash_value ^= byte  # XOR with the byte
            hash_value *= fnv_prime  # Multiply by the prime
            hash_value &= 0xffffffff  # Ensure 32-bits overflow
        
        return hash_value

    def insert_bloom(self, data):
        hash = BloomFilter.FNV_hash(data.strip().encode())
        self.bit_array[hash % self.size] = 1
        
    def query_bloom(self, data):
        hash = BloomFilter.FNV_hash(data.strip().encode())
        if self.bit_array[hash % self.size] == 1: 
            return True
        return False

    def save(self, filename):
        try:
            with open(filename, 'wb') as f:
                # Save parameters and filter data
                pickle.dump((self.num_hashes, self.size, self.bit_array), f)
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as f:
                num_hashes, size, data = pickle.load(f)
                self.size = size
                self.num_hashes = num_hashes
                self.bit_array = data
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"An error occurred while loading the file: {e}")
