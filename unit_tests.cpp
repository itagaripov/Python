#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include "data_structures.h"
using ::testing::Return;
template <typename T> class MockQueue : public IQueue<T> {
public: MOCK_METHOD(void, push, (const T& value), (override)); MOCK_METHOD(T, pop, (), (override));
};
TEST(QueueInterfaceTest, PushAndPopFIFOOrder) {
    MockQueue<int> queue;
    EXPECT_CALL(queue, push(10)).Times(1);
    EXPECT_CALL(queue, pop()).WillOnce(Return(10));
    queue.push(10);
    EXPECT_EQ(queue.pop(), 10);
}
int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv); return RUN_ALL_TESTS();
}
