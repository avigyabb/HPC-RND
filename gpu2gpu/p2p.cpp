// g++ p2p.cpp && ./a.out
#include <cuda_runtime.h>
#include <iostream>

int main() {
    int device1 = 0; // Device ID for GPU 1
    int device2 = 1; // Device ID for GPU 2

    int can_access_peer = 0;
    cudaError_t err;

    // Check if peer access is possible
    err = cudaDeviceCanAccessPeer(&can_access_peer, device1, device2);
    if (err != cudaSuccess) {
        std::cerr << "Error checking peer access: " << cudaGetErrorString(err) << std::endl;
        return -1;
    }

    std::cout << "Success!" << std::endl;

    // if (can_access_peer) {
    //     // Enable peer access
    //     err = cudaSetDevice(device1); // Set the current device
    //     if (err != cudaSuccess) {
    //         std::cerr << "Error setting device: " << cudaGetErrorString(err) << std::endl;
    //         return -1;
    //     }

    //     err = cudaDeviceEnablePeerAccess(device2, 0);
    //     if (err != cudaSuccess) {
    //         std::cerr << "Error enabling peer access: " << cudaGetErrorString(err) << std::endl;
    //         return -1;
    //     }

    //     std::cout << "Peer access enabled between Device " << device1 << " and Device " << device2 << std::endl;
    // } else {
    //     std::cout << "Peer access not supported between Device " << device1 << " and Device " << device2 << std::endl;
    // }

    return 0;
}
