import threading
import queue



def main():

    num_devices = torch.cuda.device_count()
    
    inference_threads = []

    cuda_stream = torch.cuda.Stream(device)
    while True:
        next_image, image_event = image_queue.get()


if __name__ == "__main__":
    main()