import glob
import os


def makeThumbNail(user, bid, category, condition, itemName, imageName='nopicture.jpg'):
	s='''<li class="span4">
		<a href="#" class="thumbnail">
			<img src="../data/images/%s" style="width: 300px; height: 200px;">
				<ul class="inline">
					<li><h3 class="text-info">%s</h3></li>
					<li><h3 class="text-success">%s$</h3></li>
				</ul>
				<ul class="inline">
					<li class="muted"><strong>Owner</strong></li>
					<li class="muted">%s</li>
				</ul>
				<ul class="inline">
					<li class="muted"><strong>Category</strong></li>
					<li class="muted">%s</li>
				</ul>
				<ul class="inline">
					<li class="muted"><strong>Condition</strong></li>
					<li class="muted">%s</li>
				</ul>
		</a>
	</li>
	''' % (imageName, itemName, bid, user, category, condition)
	return s

print makeThumbNail('user', 'bid', 'category', 'condition', 'itemName', 'imageName')
