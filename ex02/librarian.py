import pip
import os

def install(package, version):
    if hasattr(pip, 'main'):
        pip.main(['install', package + '==' + version])
    else:
        pip._internal.main(['install', package + '==' + version])

# Example
# if __name__ == '__main__':
#     install('argh')


if __name__ == '__main__':
	env_path = '/Users/dmadelei/Documents/Piscine-Python-for-Data-Science/env'		
	if not str(os.environ['VIRTUAL_ENV']):
		raise ValueError('asdfg')
	if (str(os.environ['VIRTUAL_ENV']) != env_path):
		raise ValueError('asdfg')
	else:
		install('six', '1.14.0')
		install('soupsieve', '2.0')
		install('termgraph', '0.2.0')
		install('wcwidth', '0.1.9')
		install('zipp', '3.1.0')
		import six
		import soupsieve
		import termgraph
		import wcwidth
		import zipp
		from pip._internal.operations import freeze
		# print (six.__version__)
		# print (soupsieve.__version__)
		# print (termgraph.__version__)
		# print (wcwidth.__version__)
		# print (zipp.__version__)
		file_name = 'requirements.txt'
		str_ret =  freeze.freeze()
		# for i in str_ret:
		# 	print(i)
		# print(str_ret)
		with open(file_name, 'w') as f:
			for i in str_ret:
				f.write(i)
				f.write('\n')
