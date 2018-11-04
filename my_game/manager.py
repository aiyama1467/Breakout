class CollisionManager:
    def check_collision(self, p, q, psize, qsize):
        if q.x <= p.x <= q.x + qsize.x:
            if q.y <= p.y <= q.y + qsize.y:
                return True
            elif q.y <= p.y + psize.y <= q.y + qsize.y:
                return True
        elif p.x <= q.x <= p.x + psize.x:

            if p.y <= q.y <= p.y + psize.y:
                return True
            elif p.y <= q.y + qsize.y <= p.y + psize.y:
                return True

        return False

    def is_collition_ball_blocks(self, ball, blocks):
        for block_l in blocks.blocks:
            for block in block_l:
                if block.is_Exist:
                    if self.check_collision(ball.pos, block.pos, ball.size, block.size):
                        block.is_Exist = False
                        return True

        return False

    def is_collition_ball_bar(self, ball, bar):
        return self.check_collision(ball.pos, bar.pos, ball.size, bar.size)