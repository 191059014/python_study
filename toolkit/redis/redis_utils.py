import redis
import rediscluster


class RedisNode:
    """
    redis节点信息
    """

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port


def get_redis_standalone(host: str = 'localhost', port: int = 6379, dbIndex: int = 0,
                         password: str = None) -> redis.Redis:
    """
    获取单机模式下redis实例
    :param host:主机
    :param port:端口
    :param dbIndex:库索引
    :param password:密码
    :return:redis实例
    """
    return redis.Redis(host=host, port=port, db=dbIndex, password=password, decode_responses=True)


def get_redis_cluster(redis_nodes: list) -> redis.Redis:
    """
    获取集群模式下的redis实例
    :param redis_nodes:
    :return:redis实例
    """
    return rediscluster.RedisCluster(startup_nodes=redis_nodes)


def get(redis_conn: redis.Redis, key: str) -> str:
    """
    获取redis中的值
    :param redis_conn: redis连接
    :param key: 缓存键
    :return: 缓存值
    """
    return redis_conn.get(key)


def set(redis_conn: redis.Redis, key, value, expire_seconds: int) -> bool:
    """
    设置缓存值
    :param redis_conn: redis连接
    :param key: 缓存键
    :param value: 缓存值
    :param expire_seconds:过期时间，单位秒
    :return: 是否设置成功
    """
    return redis_conn.set(key, value, ex=expire_seconds)


def delete(redis_conn: redis.Redis, key) -> int:
    """
    删除缓存
    :param redis_conn: redis连接
    :param key: 缓存键
    :return: 删除的个数
    """
    return redis_conn.delete(key)


def get_expire(redis_conn: redis.Redis, key) -> int:
    """
    获取过期时间
    :param redis_conn: redis连接
    :param key: 缓存键
    :return: 过期时间，单位秒
    """
    return redis_conn.ttl(key)


if __name__ == "__main__":
    redis_conn = get_redis_standalone()
    set(redis_conn, 'test_key', 'test_value', 60)
    print(get(redis_conn, 'test_key'))
    print(get_expire(redis_conn, 'test_key'))
    delete(redis_conn, 'test_key')
    redis_conn.close()
