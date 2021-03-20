from django.db import models
import time

# Branch Model
class Branch(models.Model):
    
    # branch office id
    id = models.PositiveIntegerField(unique=True, help_text='Please enter the branch id', primary_key=True)
    
    # Name of the branch (Belgium branch, Sweden, or ), but it is not the location
    name = models.CharField(max_length=256, verbose_name='Branch Name')

    # Location of the branch ( for simplicity it has been made as string/varchar)
    location = models.CharField(max_length=256, verbose_name = 'location')

    # Ip address of the branch server that can access the headquarter Ip server
    branch_ip = models.CharField(max_length=120, verbose_name = 'Branch server ip', help_text = 'Allowed Ip Address of the branch')

    def __str__(self):
        return self.name

# Daily revenu report
class DailyRevenu(models.Model):
    
    # Id of the branch sending the revenu
    Branch = models.ForeignKey(Branch, null=True, blank=True, on_delete=models.DO_NOTHING)

    # date of the report send from the branch office
    date = models.PositiveIntegerField(verbose_name='Datetime Unix',default=int(time.time()))
    # value of the revenue of the day
    revenu = models.FloatField(max_length=150,verbose_name='Revenus in Dollar$')

    # loses of the day
    loses = models.FloatField(max_length=150, verbose_name='Amount of losses in Dollar$')

    def __str__(self):
        return self.id