# # Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own workers.
# You should implement a method that allows you to add workers to a Boss. You're not allowed to add instances of Boss class to
# workers'   list directly via access to attribute, use getters and setters instead!
#
# You can refactor the existing code.
class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []
    def add_worker(self,work_inst):
        if work_inst.boss.name == self.name:
            self.workers.append(work_inst.name)
            print(f'Worker: {work_inst.name} is added to Boss {work_inst.boss.name} list')
        else:
            print('No workers were added to boss list')
    def __str__(self):
        return f'Boss_id: {str(self.id)},Bossname: {self.name}, company: {self.company}'
    def print_list_of_workers(self):
        for i in self.workers:
            print('worker:',i,end=' ')

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss
    @property
    def boss_inst(self):
        return self.boss
    @boss_inst.setter
    def boss_inst(self,value):
        self.boss = value
    def __str__(self):
        return f'Worker\'s id_:{str(self.id)}, worker\'s name: {self.name}, company: {self.company}, boss: {self.boss}'
    def check_boss(self,instanse,cls):
        if isinstance(instanse,cls):
            print('This instance is Boss.')
        else:
            print('This instance is not Boss.')
boss1 = Boss(123541,'Jack Monson','"JSK Horizont"')
boss2 = Boss(542165,'Sergiy Dmitryk',"JSK Diamant")
print(boss1)
work1 = Worker(725354,"Boris Johnson","JSK Horizont",boss1)
work2 = Worker(874545,"Jack Savoretti","TOV Mirazh",boss2)
print(work1)
work1.check_boss(work1,Boss)
work1.check_boss(boss2,Boss)
work1.boss_inst = boss2
print(work1)
boss1.add_worker(work1) # check if the instanse of worker "work1" has boss instance "boss1"
boss2.add_worker(work1)
boss2.add_worker(work2)
boss2.print_list_of_workers()

