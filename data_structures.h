#pragma once
#include <stdexcept>
template <typename T> class IQueue {
public: virtual ~IQueue() = default; virtual void push(const T& value) = 0; virtual T pop() = 0;
};
template <typename T> class IHeap {
public: virtual ~IHeap() = default; virtual void push(const T& value) = 0; virtual T pop() = 0;
};
template <typename T> class IBinaryTree {
public: virtual ~IBinaryTree() = default; virtual void push(const T& value) = 0; virtual T pop() = 0; virtual bool search(const T& value) const = 0;
};
